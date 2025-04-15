# Converge

**Converge** is a customizable, neuroscience-informed framework for goal setting, habit building, and intentional daily routines. Designed to reduce cognitive load by bringing a variety of meaningful actions into a common space to increase their visibility . Converge serves as a gentle guide for growth-oriented individuals — without promoting hustle culture or toxic productivity.

---

## Features

- A modular **goal-setting system** that breaks down complex objectives into trackable milestones and action items
- Personalized **routine builder** (AM, PM, Flex, and Intention routines) linked to recommended self-care practices
- Value Map, Priority Map, and Interest Map to guide users into meaningful goal selection
- Smart **survey system** to dynamically assess user needs, patterns, and focus areas
- Specialized modules for ADHD, anxiety, digital overuse, dopamine reset, and more
- **Habit Anchors**, **Strategies**, and **Barriers** to reinforce behavioral design
- Progress tracking, streaks, and gamification elements without competitiveness
- Flexible goal types: active, collaborative, self-care, supportive, etc.

---

## Philosophy

Converge is designed for users who:
- Want a force multiplier to organize their life and decrease cognitive load
- Want clarity without rigidity
- Crave progress without pressure
- Seek purpose but feel overwhelmed by distractions
- Want to focus on self-care, focus, motivation, and alignment with long-term vision

Converge is not about “hustling harder” — it’s about sustainable progress and **converging** on what truly matters.

---

##  Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML / Vanilla JS (React planned)
- **Database:** MySQL 8.x
- **Modeling:** MySQL Workbench + forward engineering
- **State:** Initially managed via Python/JS, with a modular refactor to follow

---

## Project Structure
converge/
│
├── app.py                      # Main Flask app entry point
├── schema/
│   ├── converge_schema.sql     # Full schema forward-engineered from Workbench
│   └── post_forward_constraints.sql  # Patch file for manual constraints
│
├── models/                     # Python classes for database tables
│   ├── goal.py
│   ├── milestone.py
│   ├── action_item.py
│   └── ...
│
├── routes/                     # Flask route controllers
│   ├── goals.py
│   ├── routines.py
│   └── ...
│
├── static/                     # Static assets (CSS, JS)
│   └── js/
│       ├── add-goal.js
│       ├── edit-milestones.js
│       └── ...
│
├── templates/                  # Jinja templates (HTML pages)
│   └── surveys/
│       ├── getting-to-know-you.html
│       └── ...
│
├── data/                       # Seed files for practices, goals, etc.
│   └── survey_seed_data.py
│
├── tests/                      # Unit tests (future use)
│
├── README.md                   # You're here
└── .env.example                # Example environment config (optional)
|

## Schema Conventions

Converge’s database schema is designed for flexibility, consistency, and extensibility.

- ✅ `snake_case` naming throughout
- ✅ `created_at` and `updated_at` timestamps on all user-generated content
- ✅ Join tables follow the `x_has_y` pattern (e.g., `users_has_goals`)
- ✅ ENUMs used where values are constrained but descriptive (e.g., `goal_type`, `routine_type`)
- ✅ Example/template data separated from user data (`routine_templates` vs `user_routines`)
- ✅ Placeholder or experimental tables prefixed with `spec_` or `placeholder_` for clarity

Naming consistency helps:
- Reduce mental friction
- Make query writing and table introspection easier
- Future-proof migration to ORM (if applicable)

---

## System Architecture

The app is built with a layered, modular approach:

### 1. **Seed Data**
- Goals, routines, practices, and strategies are pre-seeded from example/template tables
- Seeds act as recommendations, not prescriptions

### 2. **User Personalization**
- Users can adopt, ignore, or build from scratch
- `user_routines`, `users_has_goals`, and `user_flex_tasks` reflect personal progress

### 3. **Guided Mapping System**
- Mapping system (Value Map, Priority Map, Interest Map) helps users determine:
  - What matters to them
  - What they want to prioritize
  - Where they’re currently out of alignment
- Leads directly into practice/routine/goal suggestions

### 4. **Behavioral Scaffolding**
- Practices link to habit anchors, strategies, and barriers
- These reinforce healthy repetition and behavioral design
- Tracks streaks, motivation, and progress without over-gamifying

---

## Roadmap

### MVP Complete or Near-Complete
- [x] Full normalized schema
- [x] Survey system with branching logic and answer mapping
- [x] Routine builder with durations and categories
- [x] Practice seeding system with categories, objectives, and relevance scores
- [x] Goal structure with milestones and action items
- [x] Flex task system for prioritization of daily tasks
- [x] Habit anchors and strategy mapping system

### 🔜 Near-Term Goals
- [ ] Clean UI for adding/editing goals, milestones, action items
- [ ] Visual streak and progress tracking
- [ ] Dashboard "At-a-Glance" tab
- [ ] Initial deployment with user authentication
- [ ] Routine templating +
