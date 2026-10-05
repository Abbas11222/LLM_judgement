# Week 4 Project Plan

## Project

**LLM-as-Judge Evaluation Framework with Human-Agreement Calibration**

## Objective

Build and validate an LLM-based evaluation system that scores insurance-related AI answers using a four-criterion rubric and measure how closely its judgments agree with human evaluation.

## Five-Line Execution Plan

1. **Define the evaluation scope and rubric** for Accuracy, Completeness, Tone, and Safety using a 1–5 anchored scoring scale.

2. **Create an evaluation dataset of at least 48 AI-generated answers** from 24 insurance questions and two answer generators.

3. **Collect human scores first**, keeping the human evaluation independent from the LLM judge, and then run the first version of the LLM judge with deterministic settings.

4. **Measure human–LLM agreement**, analyze disagreements, and test whether answer length or answer position influences the judge.

5. **Improve the judge prompt once**, rerun the evaluation, and compare Version 2 against Version 1 using the same evaluation methodology.

## Measurable Success Target

The primary target is:

> **Achieve a Quadratic Weighted Kappa (QWK) of at least 0.60 between the LLM judge and human evaluator, while demonstrating measurable improvement from Judge Version 1 to Judge Version 2.**

Additional metrics will include:

* Unweighted Cohen's kappa
* Quadratic Weighted Kappa
* Spearman correlation
* Exact agreement
* Within-one-score agreement
* Confusion matrix
* Bias measurements

## Dataset Target

| Component           |            Target |
| ------------------- | ----------------: |
| Insurance questions |                24 |
| Answer generators   |                 2 |
| Minimum AI answers  |                48 |
| Evaluation criteria |                 4 |
| Score range         |               1–5 |
| Judge versions      |                 2 |
| Human evaluation    |          Required |
| Bias experiments    | Length + Position |

## Experimental Principle

The project will follow a controlled evaluation process.

Human scores will be collected before the LLM judge receives access to evaluation results.

The judge will receive only the information required to evaluate an answer:

* Question
* Answer
* Evaluation rubric

Human scores will not be included in the judge prompt.

## Development and Evaluation Split

Where practical, a small development subset will be used when improving the judge prompt.

The final evaluation results should not be repeatedly used to tune the judge prompt, because doing so could make the reported agreement artificially optimistic.

Therefore, the project will distinguish between:

* **Development data** — used for prompt improvement
* **Evaluation data** — used for final measurement
