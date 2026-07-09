# PermitFlow AI

PermitFlow AI is a full-stack building permit and construction compliance management platform designed to help homeowners, designers, contractors, and project teams organize permit projects, track documentation, monitor project readiness, and identify potential risk factors.

The project combines modern web development, cloud-ready architecture, data analytics, and explainable AI concepts.

## Project Status

🚧 Currently under active development.

Current progress:

- [x] React + TypeScript frontend initialized
- [x] FastAPI backend initialized
- [x] PostgreSQL database configured with Docker
- [x] SQLAlchemy database connection created
- [x] Project database model created
- [ ] Project CRUD API
- [ ] Create Project frontend form
- [ ] Project dashboard
- [ ] Permit checklist engine
- [ ] Explainable risk scoring
- [ ] User authentication
- [ ] AWS S3 document storage
- [ ] Machine learning risk model
- [ ] Production deployment

## Features

Planned core features include:

- Create and manage building permit projects
- Track project status and permit readiness
- Generate project-specific document checklists
- Monitor missing or incomplete requirements
- Calculate project completion percentages
- Identify project risk factors
- Provide explainable risk classifications
- Upload and organize permit documentation
- Display analytics and project dashboards
- Support future AI-assisted project guidance

## Example Project Types

PermitFlow AI is designed to support project categories such as:

- Basement renovations
- Additional dwelling units
- Decks
- Garages
- Building additions
- Interior renovations
- Other residential construction projects

## Technology Stack

### Frontend

- React
- TypeScript
- Vite
- CSS
- Axios

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- PostgreSQL

### Infrastructure

- Docker
- Docker Compose
- GitHub

### Planned Cloud Services

- AWS S3
- AWS RDS
- AWS CloudWatch

### Planned AI and Data Features

- pandas
- scikit-learn
- Decision Tree classification
- Explainable risk scoring
- Project analytics

## Architecture

```text
┌──────────────────────────────┐
│     React + TypeScript       │
│          Frontend            │
└──────────────┬───────────────┘
               │
               │ HTTP / JSON
               ▼
┌──────────────────────────────┐
│       FastAPI Backend        │
│                              │
│ Projects                     │
│ Checklists                   │
│ Risk Analysis                │
│ Documents                    │
└──────────────┬───────────────┘
               │
               │ SQLAlchemy
               ▼
┌──────────────────────────────┐
│         PostgreSQL           │
│                              │
│ Projects                     │
│ Users                        │
│ Checklist Items              │
│ Risk Assessments             │
└──────────────────────────────┘