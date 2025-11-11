INSERT INTO subjects (name) VALUES
  ('Matemática'), ('Física'), ('Química')
ON DUPLICATE KEY UPDATE name = VALUES(name);

INSERT INTO topics (subject_id, name)
SELECT s.id, t.topic_name
FROM subjects s
JOIN (
  SELECT 'Matemática' AS subject_name, 'Derivadas' AS topic_name UNION ALL
  SELECT 'Matemática', 'Integrais' UNION ALL
  SELECT 'Física',     'Cinemática' UNION ALL
  SELECT 'Química',    'Estequiometria'
) t ON t.subject_name = s.name
ON DUPLICATE KEY UPDATE name = VALUES(name);
