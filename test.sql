INSERT INTO tutor_tutor (name, email, description, avatar_image, instrument_id, music_styles_id, updated_on, created_on) VALUES
    ('John Doe', 'john.doe@example.com', 'Experienced guitar teacher with a passion for classical and rock music.', 'https://cloudinary.com/images/john_doe_avatar.jpg', 1, 2, '2024-01-15 12:30:00', '2024-01-15 12:30:00'),
    ('Alice Johnson', 'alice.johnson@example.com', 'Piano virtuoso offering lessons in jazz and contemporary styles.', 'https://cloudinary.com/images/alice_johnson_avatar.jpg', 2, 3, '2024-01-15 13:45:00', '2024-01-15 13:45:00'),
    ('Bob Smith', 'bob.smith@example.com', 'Versatile music instructor specializing in brass instruments and marching band.', 'https://cloudinary.com/images/bob_smith_avatar.jpg', 3, 1, '2024-01-15 14:20:00', '2024-01-15 14:20:00'),
    ('Emma Davis', 'emma.davis@example.com', 'Passionate vocal coach with expertise in pop and classical singing.', 'https://cloudinary.com/images/emma_davis_avatar.jpg', 1, 4, '2024-01-15 15:10:00', '2024-01-15 15:10:00'),
    ('Michael Brown', 'michael.brown@example.com', 'Dedicated drum teacher with a focus on rhythm and percussion techniques.', 'https://cloudinary.com/images/michael_brown_avatar.jpg', 2, 5, '2024-01-15 16:00:00', '2024-01-15 16:00:00');


INSERT INTO tutor_instrument (name, color) VALUES
    ('Guitar', 'FFA500'),
    ('Piano', '0000FF'),
    ('Vocals', 'FF1493'),
    ('Trumpet', 'FFD700'),
    ('Drums', '808080');


INSERT INTO tutor_musicstyle (name, color) VALUES
    ('Classical', '9932CC'),
    ('Jazz', 'FFD700'),
    ('Pop', 'FF4500'),
    ('Rock', '00FFFF'),
    ('Country', '8B4513');