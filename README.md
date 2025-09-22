
# Volt-Source Energy: The AI Co-Pilot for Smarter Growth & Safer Revenue

**Elevator Pitch:** An AI-driven platform that helps utility companies transform vast customer data into predictable revenue and reduced risk by identifying high-value growth opportunities and preventing bad debt before it happens.

## Project Summary

This project is an innovative data analytics solution built for the **Tableau Next Hackathon 2025**. We have designed and prototyped an intelligent customer value and risk platform for a modern utility company, "Volt-Source Energy," to address three core industry challenges: **customer churn, bad debt risk, and a lack of new revenue streams**.

The platform's core architecture seamlessly integrates customer data from Salesforce CRM with massive-scale smart meter data processed by Data Cloud. By leveraging the analytical power of Tableau Next and the conversational AI capabilities of Agentforce, this solution creates a complete business loop from **analysis and insight** to **prediction and alerts**, and finally to **automated decision-making**.

## Key Features

Our platform is composed of three logically progressive modules:

### Module 1: Intelligent Pricing Analysis & Churn Prevention

* **Objective: Retain Customers.** This module forms the foundation of customer trust. The platform deeply analyzes each customer's unique energy consumption "fingerprint" to proactively identify those who are on sub-optimal, more expensive pricing plans.
* **Proactive Care:** For these high-risk customers, the system automatically recommends a better, cost-saving plan and uses Agentforce to create follow-up tasks for the customer service team. This proactive approach to customer care significantly increases loyalty and reduces churn.

### Module 2: Credit Management & Smart Collections (End-to-End)

* **Objective: Control Risk.** This module acts as the business's financial firewall. It establishes an automated risk management system covering the entire customer lifecycle.
* **Automated Workflow:**
    * **Proactive Assessment:** At sign-up, an initial credit score is generated for new users based on demographic data and regional risk, triggering differentiated onboarding strategies.
    * **Dynamic Monitoring:** Using Data Cloud, a "Dynamic Credit Score" is calculated daily for each customer and automatically written back to their Salesforce record, enabling a true 360-degree risk view.
    * **Automated Action:** A Salesforce Flow runs daily, identifying overdue accounts and automatically triggering tiered collection actions (e.g., sending email reminders, creating manual call tasks) based on the number of overdue days.

### Module 3: EV Owner Smart Charging Package

* **Objective: Create Growth.** This is the key module for shifting from defense to offense. The platform identifies "Potential EV Owners"—a high-value customer segment—by analyzing the unique data fingerprint of EV charging (sustained, stable, high-power nightly usage).
* **Precision Marketing:** The platform then enables highly targeted marketing for a value-added service package, which includes a smart EV charger and an exclusive "Smart Off-Peak" tariff. The Agentforce assistant allows the marketing team to launch personalized campaigns with a single command, opening up new, high-margin revenue streams.

## Technology Stack

* **Core Platform:** Salesforce, Tableau Next
* **Data Processing & Integration:** Salesforce Data Cloud
    * **Data Streams:** For ingesting massive-scale, hourly smart meter data.
    * **Data Transforms:** For backend data preparation and complex aggregations (e.g., calculating dynamic credit scores and user profiles).
    * **Activations:** For automatically writing insights calculated in Data Cloud (like credit scores and profile tags) back into the Salesforce CRM.
* **Analysis & Visualization:** Tableau Next
    * **Semantic Data Model (SDM):** For integrating multi-source data and creating business logic with calculated fields.
    * **Dashboards:** For providing visual decision support for different personas (Executive, Collections Manager, Marketing Director).
* **Intelligent Interaction:** Agentforce for Analytics (Concierge)
    * Serves as the AI co-pilot for natural language queries, translating insights directly into business actions (e.g., creating tasks).
* **Data Fabrication:** Python (Pandas, Numpy)
    * Used to generate high-quality, synthetic datasets with embedded business logic, multiple user personas, and realistic scenarios.

## How to Run & Demo

1.  **Environment Setup:** In a Salesforce org, create all required custom objects and fields as per the project checklist.
2.  **Data Generation:** Run the provided Python scripts to generate all necessary `.csv` data files.
3.  **Data Ingestion:**
    * Import the core CRM data files into Salesforce using the **Data Import Wizard**.
    * Ingest the large-scale smart meter data file into Data Cloud using **Data Streams**.
4.  **Model Construction:**
    * In Data Cloud, run the **Data Transforms** to pre-calculate key metrics.
    * In Tableau Next, build the **Semantic Data Model** to join all data objects and create the final calculated fields.
5.  **Visualization & Demo:**
    * In Tableau Next, create the three core dashboards.
    * Frame the final demo around the "Day in the Life of a Utility Executive" storyline, using **Agentforce** to ask questions that seamlessly connect the features of all three modules, showcasing a complete "Retain -> Control -> Grow" decision-making process.
