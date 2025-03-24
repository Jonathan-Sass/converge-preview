-- post_forward_constraints.sql
-- Run this manually after forward engineering from your ERD

USE converge_schema;

-- Enforce mutually exclusive milestone_id vs. action_item_id in user_flex_tasks
ALTER TABLE user_flex_tasks
DROP CONSTRAINT IF EXISTS chk_only_one_task_type;

ALTER TABLE user_flex_tasks
ADD CONSTRAINT chk_only_one_task_type
CHECK (
  (milestone_id IS NOT NULL AND action_item_id IS NULL)
  OR
  (milestone_id IS NULL AND action_item_id IS NOT NULL)
);
