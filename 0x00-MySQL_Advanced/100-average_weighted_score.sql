--Average weighted score task
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE weighted_avg_score FLOAT;

    SELECT SUM(c.score * p.weight) / SUM(p.weight)
    INTO weighted_avg_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = weighted_avg_score
    WHERE id = user_id;
END //

DELIMITER ;