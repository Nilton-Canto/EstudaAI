-- -----------------------------------------------------------------------------
-- EstudaAI - schema MySQL 8 (InnoDB, utf8mb4)
-- -----------------------------------------------------------------------------
SET NAMES utf8mb4;
SET sql_mode = 'STRICT_ALL_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO';

-- =============================================================================
-- TABELAS (ENUMs via ENUM nas colunas)
-- =============================================================================

-- users
CREATE TABLE IF NOT EXISTS users (
  id            CHAR(36)      NOT NULL,
  name          VARCHAR(120)  NULL,
  email         VARCHAR(255)  NOT NULL,
  password_hash VARCHAR(255)  NULL,
  role          ENUM('USER','ADMIN') NOT NULL DEFAULT 'USER',
  created_at    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- subjects
CREATE TABLE IF NOT EXISTS subjects (
  id          INT            NOT NULL AUTO_INCREMENT,
  name        VARCHAR(120)   NOT NULL,
  created_at  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_subjects_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- topics
CREATE TABLE IF NOT EXISTS topics (
  id          INT            NOT NULL AUTO_INCREMENT,
  subject_id  INT            NOT NULL,
  name        VARCHAR(120)   NOT NULL,
  created_at  DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_topics_subject_name (subject_id, name),
  KEY idx_topics_subject (subject_id),
  CONSTRAINT fk_topics_subject
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- contents
CREATE TABLE IF NOT EXISTS contents (
  id          CHAR(36)     NOT NULL,
  user_id     CHAR(36)     NOT NULL,
  subject_id  INT          NULL,
  topic_id    INT          NULL,
  title       VARCHAR(200) NULL,
  raw_text    LONGTEXT     NULL,
  source_type VARCHAR(20)  NULL,
  created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_contents_user_created (user_id, created_at),
  KEY idx_contents_subject_topic (subject_id, topic_id),
  CONSTRAINT fk_contents_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_contents_subject
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
    ON DELETE SET NULL ON UPDATE RESTRICT,
  CONSTRAINT fk_contents_topic
    FOREIGN KEY (topic_id) REFERENCES topics(id)
    ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- files
CREATE TABLE IF NOT EXISTS files (
  id          CHAR(36)   NOT NULL,
  user_id     CHAR(36)   NOT NULL,
  content_id  CHAR(36)   NULL,
  url         TEXT       NOT NULL,
  mime        VARCHAR(80) NULL,
  created_at  DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_files_user (user_id),
  KEY idx_files_content (content_id),
  CONSTRAINT fk_files_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_files_content
    FOREIGN KEY (content_id) REFERENCES contents(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ai_requests
CREATE TABLE IF NOT EXISTS ai_requests (
  id          CHAR(36)    NOT NULL,
  user_id     CHAR(36)    NOT NULL,
  content_id  CHAR(36)    NULL,
  provider    ENUM('OPENAI','ANTHROPIC','GEMINI') NOT NULL,
  model       VARCHAR(80) NULL,
  prompt      LONGTEXT    NULL,
  status      ENUM('QUEUED','RUNNING','OK','ERROR') NOT NULL DEFAULT 'QUEUED',
  cost_usd    DECIMAL(10,4) NULL,
  created_at  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_air_user_created (user_id, created_at),
  KEY idx_air_content (content_id),
  CONSTRAINT fk_air_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_air_content
    FOREIGN KEY (content_id) REFERENCES contents(id)
    ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- artifacts
CREATE TABLE IF NOT EXISTS artifacts (
  id            CHAR(36)   NOT NULL,
  ai_request_id CHAR(36)   NOT NULL,
  type          ENUM('FLASHCARD','SUMMARY','EXERCISE') NOT NULL,
  payload       JSON       NOT NULL,
  difficulty    INT        NULL,
  created_at    DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_artifacts_air_type (ai_request_id, type),
  CONSTRAINT fk_artifacts_air
    FOREIGN KEY (ai_request_id) REFERENCES ai_requests(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- trails
CREATE TABLE IF NOT EXISTS trails (
  id          CHAR(36)    NOT NULL,
  creator_id  CHAR(36)    NOT NULL,
  title       VARCHAR(160) NOT NULL,
  description TEXT        NULL,
  visibility  ENUM('PRIVATE','UNLISTED','PUBLIC') NOT NULL DEFAULT 'PRIVATE',
  status      ENUM('DRAFT','PUBLISHED','ARCHIVED') NOT NULL DEFAULT 'DRAFT',
  is_default  BOOLEAN     NOT NULL DEFAULT FALSE,
  created_at  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_trails_creator (creator_id),
  CONSTRAINT fk_trails_creator
    FOREIGN KEY (creator_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- trail_steps
CREATE TABLE IF NOT EXISTS trail_steps (
  id          CHAR(36)    NOT NULL,
  trail_id    CHAR(36)    NOT NULL,
  position    INT         NOT NULL,
  title       VARCHAR(160) NULL,
  description TEXT        NULL,
  recommended_duration_min INT NULL,
  created_at  DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_trail_steps_trail_position (trail_id, position),
  KEY idx_steps_trail (trail_id),
  CONSTRAINT fk_steps_trail
    FOREIGN KEY (trail_id) REFERENCES trails(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- step_resources
CREATE TABLE IF NOT EXISTS step_resources (
  id          CHAR(36)   NOT NULL,
  step_id     CHAR(36)   NOT NULL,
  artifact_id CHAR(36)   NULL,
  external_url TEXT      NULL,
  label       VARCHAR(160) NULL,
  created_at  DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_resources_step (step_id),
  KEY idx_resources_artifact (artifact_id),
  CONSTRAINT fk_resources_step
    FOREIGN KEY (step_id) REFERENCES trail_steps(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_resources_artifact
    FOREIGN KEY (artifact_id) REFERENCES artifacts(id)
    ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- user_trails
CREATE TABLE IF NOT EXISTS user_trails (
  id          CHAR(36)   NOT NULL,
  user_id     CHAR(36)   NOT NULL,
  trail_id    CHAR(36)   NOT NULL,
  started_at  DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  completed_at DATETIME  NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_user_trails_user_trail (user_id, trail_id),
  KEY idx_user_trails_user (user_id),
  KEY idx_user_trails_trail (trail_id),
  CONSTRAINT fk_user_trails_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_user_trails_trail
    FOREIGN KEY (trail_id) REFERENCES trails(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- progress
CREATE TABLE IF NOT EXISTS progress (
  id            CHAR(36)   NOT NULL,
  user_trail_id CHAR(36)   NOT NULL,
  step_id       CHAR(36)   NOT NULL,
  state         VARCHAR(20) NULL,
  score         DECIMAL(5,2) NULL,
  updated_at    DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_progress_usertrail_step (user_trail_id, step_id),
  KEY idx_progress_usertrail (user_trail_id),
  KEY idx_progress_step (step_id),
  CONSTRAINT fk_progress_usertrail
    FOREIGN KEY (user_trail_id) REFERENCES user_trails(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_progress_step
    FOREIGN KEY (step_id) REFERENCES trail_steps(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- study_sessions
CREATE TABLE IF NOT EXISTS study_sessions (
  id         CHAR(36)   NOT NULL,
  user_id    CHAR(36)   NOT NULL,
  trail_id   CHAR(36)   NULL,
  step_id    CHAR(36)   NULL,
  started_at DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ended_at   DATETIME   NULL,
  elapsed_ms INT        NULL,
  PRIMARY KEY (id),
  KEY idx_sessions_user_started (user_id, started_at),
  KEY idx_sessions_trail (trail_id),
  KEY idx_sessions_step (step_id),
  CONSTRAINT fk_sessions_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_sessions_trail
    FOREIGN KEY (trail_id) REFERENCES trails(id)
    ON DELETE SET NULL ON UPDATE RESTRICT,
  CONSTRAINT fk_sessions_step
    FOREIGN KEY (step_id) REFERENCES trail_steps(id)
    ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- recommendations
CREATE TABLE IF NOT EXISTS recommendations (
  id         CHAR(36)   NOT NULL,
  user_id    CHAR(36)   NOT NULL,
  trail_id   CHAR(36)   NULL,
  reason     TEXT       NULL,
  created_at DATETIME   NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_reco_user (user_id),
  KEY idx_reco_trail (trail_id),
  CONSTRAINT fk_reco_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT fk_reco_trail
    FOREIGN KEY (trail_id) REFERENCES trails(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
