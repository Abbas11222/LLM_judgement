# Week 4 — Scope Statement

## Project Title

**LLM-as-Judge Evaluation Framework with Human-Agreement Calibration for a Family-Owned Insurance Brokerage**

## 1. Project Purpose

The purpose of this project is to build an evaluation framework for measuring the quality of AI-generated answers for a family-owned insurance brokerage.

Instead of evaluating an AI system only by whether it produces an answer, this project evaluates the quality of those answers using two evaluators:

1. A human evaluator
2. An LLM acting as an automated judge

The scores produced by the LLM judge will be compared with the human scores to determine how closely the automated evaluator agrees with human judgment.

The project will also investigate whether the LLM judge is affected by factors such as answer length or the position/order of answers.

## 2. In-Scope Topics

The evaluation dataset will focus on client-facing insurance questions involving relatively common insurance concepts, including:

* Personal auto insurance
* Homeowners insurance
* Renters insurance
* Basic life insurance concepts
* General liability insurance
* Business Owner's Policy (BOP)
* Deductibles
* Premiums
* Coverage explanations
* Policy terminology
* Renewal processes
* General claims processes

The questions will be designed to represent situations in which an insurance brokerage might provide general educational information to customers.

## 3. Out-of-Scope Topics

The system will not be used to make actual insurance or legal decisions.

The following areas are explicitly outside the scope:

* Providing insurance quotes
* Binding or purchasing coverage
* Making actual claims decisions
* Determining whether a claim will be approved
* Legal advice
* Tax advice
* State-specific regulatory rulings
* Personalized underwriting decisions
* Definitive statements about whether a specific policy covers a specific loss

The system is an **evaluation framework**, not an insurance decision-making system.

## 4. Evaluation Scope

The project will evaluate at least:

**24 questions × 2 answer generators = 48 AI-generated answers**

Each answer will be evaluated using four criteria:

1. Accuracy
2. Completeness
3. Tone
4. Safety

Each criterion will use a **1–5 ordinal scale**.

The same answers will be evaluated by:

* Human scoring
* LLM-as-judge scoring

The two sets of scores will then be compared using statistical agreement measures.

## 5. Main Success Criteria

The project will be considered successful if it:

* Produces at least 48 AI-generated answers.
* Uses a clearly defined four-criterion rubric.
* Collects human scores before exposing those scores to the automated judge.
* Produces structured LLM judge scores.
* Measures human–LLM agreement.
* Tests length and position bias.
* Identifies disagreements between human and LLM evaluation.
* Improves the judge prompt from Version 1 to Version 2 based on observed disagreements.
* Provides a reproducible evaluation pipeline.
* Provides a small interactive demonstration using Streamlit.

## 6. Important Limitation

Human scores will be treated as the **reference evaluator for this project**, not as an absolute definition of objective truth.

The goal is therefore not to prove that the LLM judge is always correct.

The goal is to measure whether the LLM judge can reproduce the judgments made by the project's human evaluator consistently and transparently.
