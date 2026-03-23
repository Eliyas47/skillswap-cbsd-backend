# PostgreSQL Component Mapping — Skill Swap Backend

This document defines how backend components connect with PostgreSQL persistence layer.

Component → Database Mapping

Auth Component
Stores login credentials and token references

User Component
Stores profile information and account metadata

Skill Component
Stores teachable and learnable skills

Swap Component
Stores exchange requests and swap workflow state

Chat Component
Stores communication messages between users

Rating Component
Stores feedback and reputation scores

Architecture Strategy

Each backend component communicates with PostgreSQL through service-layer logic following CBSD layered architecture principles.

Result

This structure supports scalable modular backend persistence design suitable for Skill Swap platform and Final Year Project reuse.