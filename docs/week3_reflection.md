# Week 3 Reflection

## Project Reviewed

**Recommendation Engine v2 — Collaborative + Content-Based Recommendation System for an Independent Elderly Care Facility**

## 1. Three Strengths Developed in Week 3

### Strength 1 — Building a Complete ML Pipeline

One strength developed during Week 3 was the ability to organize an ML project as a complete pipeline rather than focusing only on a model.

The recommendation engine involved multiple components including data loading, preprocessing, content-based recommendation, collaborative filtering, hybrid recommendation, evaluation, and interaction logging.

This helped me understand how different ML components work together to form an actual application.

### Strength 2 — Combining Multiple Recommendation Signals

Another strength was understanding the difference between content-based and collaborative filtering and combining their signals into a hybrid recommendation approach.

This gave me practical experience with designing a recommendation system instead of implementing only one recommendation technique.

### Strength 3 — Connecting ML Logic to an Application

The Week 3 project also strengthened my ability to connect Python ML logic with a user-facing Flask application.

The system was designed to load data, generate recommendations, receive user interactions, and store interaction information.

This helped me understand that an ML project needs application-level integration and data flow in addition to the model itself.

## 2. Two Gaps Identified

### Gap 1 — Evaluation Methodology

A major gap identified from Week 3 was that evaluation focused primarily on whether the recommendation system produced useful results, rather than deeply studying how evaluation itself should be designed and validated.

I had not yet worked extensively with statistical agreement measures or human-versus-model evaluation.

Week 4 addresses this gap by introducing formal agreement measurement between human evaluation and an LLM judge.

### Gap 2 — Systematic Evaluation of Generative AI

Another gap was limited experience evaluating the quality of generated natural-language outputs.

Recommendation systems mainly produce ranked recommendations, while Week 4 requires evaluating complete natural-language answers across multiple qualitative criteria.

This introduces a new challenge: converting subjective quality judgments into a structured rubric and then measuring how closely an automated evaluator agrees with those judgments.

## 3. New Skill for Week 4

The main new skill for Week 4 is:

> **LLM-as-a-Judge evaluation with human-agreement calibration.**

This includes:

* Designing an evaluation rubric
* Creating anchored scoring criteria
* Using an LLM as an automated evaluator
* Comparing LLM scores with human scores
* Understanding Cohen's kappa
* Understanding weighted kappa
* Using Quadratic Weighted Kappa for ordinal scores
* Detecting evaluation bias
* Performing error and disagreement analysis
* Improving an evaluation prompt based on evidence

## 4. What Changes from Week 3 to Week 4?

Week 3 primarily focused on **building a recommendation system**.

Week 4 focuses on **building a system that evaluates AI-generated outputs**.

Therefore, Week 4 introduces a different engineering problem:

> Instead of asking "Can my model generate a useful result?", I am asking "Can an automated evaluator reliably judge the quality of AI-generated results in a way that agrees with human judgment?"
