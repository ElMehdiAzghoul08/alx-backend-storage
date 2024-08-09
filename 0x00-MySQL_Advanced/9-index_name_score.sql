--Optimize search and score task
CREATE INDEX idx_name_first_score ON names (name(1), score);