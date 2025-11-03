CREATE TYPE task_status AS ENUM ('pending', 'in_progress', 'completed', 'cancelled');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username Text UNIQUE NOT NULL,
    password Text NOT NULL,
    email Text UNIQUE,
	 created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);


CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users (id) ON DELETE CASCADE,
    task_name Text NOT NULL,
    due_date TIMESTAMP,
    description TEXT,
    status task_status NOT NULL DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE subtask (
    id SERIAL PRIMARY KEY,
    task_id INT NOT NULL REFERENCES tasks (id) ON DELETE CASCADE,
    name Text NOT NULL,
    status task_status NOT NULL DEFAULT 'pending',
    due_date TIMESTAMP,
    description TEXT,
	created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
