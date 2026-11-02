# Business Problem and Requirements

## 1. Business Problem
Takealot is an e-commerce company that processes and delivers a large number of customer orders. During the packaging and dispatch process, parcels may develop visible external damages such as dents, tears, holes or crushed areas. 

When a customer later reports that a parcel arrived damaged, it may be difficult to detemine whether the damge occured before the parcel was dispatched or during the delivery process. Without the record of the parcel's condition before dispatch, it can also be dificult to investigate damage-related complaints.

The proposed system aims to address this problem by using artificial intelligence and computer vision to inspect parcel inside the takealot warehouse before they are dispatched.

## 2. Proposed Solution

The proposed solution is an AI-based parcel damage detection system that uses cameras and computer vision to inspect the external condition of parcels before they leave the Takealot warehouse.

Parcels will move through a scanning area on a conveyor belt. A camera will automatically capture an image of each parcel, and the AI system will analyse the image to determine whether the visible external packaging is **Damaged** or **Intact**.

If the parcel is detected as damaged, it will be removed from the normal conveyor flow and sent to staff for inspection and repackaging if necessary. If the parcel is detected as intact, it will continue through the normal dispatch process.

The system will also provide a visual record of the parcel's condition before dispatch, which can support investigations into future damage-related complaints.

## 3. Business Objectives

The main objectives of the proposed system are to:

- Detect visible damage to parcel packaging before parcels leave the warehouse.
- Identify parcels that require staff inspection before dispatch.
- Create a record of the parcel's external condition before dispatch.
- Support Takealot when investigating damage-related customer complaints.
- Reduce unnecessary returns, refunds and replacement costs caused by disputed damage claims.
- Improve the overall parcel handling and quality-control process.

## 4. Stakeholders

The main stakeholders affected by the proposed system are:

- **Takealot management:** Interested in improving parcel quality control and reducing costs related to damage claims, returns and refunds.
- **Warehouse staff:** Use the system results to identify parcels that require inspection before dispatch.
- **Customers:** Benefit from improved parcel quality control and a clearer process for investigating damage-related complaints.
- **Customer service and returns teams:** Can use the recorded parcel condition to support investigations of damage-related claims.
- **Dispatch and delivery operations:** Receive parcels that have passed the warehouse damage inspection process.

## 5. Functional Requirements

The system should:

- Capture images of parcels as they pass through the warehouse scanning area.
- Analyse parcel images using a computer vision model.
- Classify parcel packaging as **Damaged** or **Intact**.
- Identify visible external damage such as tears, holes, dents and crushed areas.
- Alert warehouse staff when a damaged parcel is detected.
- Record the parcel's inspection result.
- Support the inspection and repackaging of damaged parcels before dispatch.
- Allow parcels to be rescanned after repackaging.

## 6. Non-Functional Requirements

The system should:

- Provide reliable and consistent damage classifications.
- Process parcel images quickly enough to support the warehouse workflow.
- Be easy for warehouse staff to use.
- Store inspection results in an organised manner.
- Be scalable to handle a large number of parcel images.
- Protect stored parcel images and any customer information that may be visible on parcel labels.## 7. Scope and Limitations

### 7.1 In Scope

The proposed system will:

- Inspect parcels inside the Takealot warehouse before dispatch.
- Capture images of parcels using a camera.
- Detect visible external damage to parcel packaging.
- Classify parcels as **Damaged** or **Intact**.
- Record the inspection result.
- Support the process of sending damaged parcels for staff inspection and repackaging.
- Allow a repackaged parcel to be inspected again before dispatch.

### 7.2 Out of Scope

The proposed system will not:

- Determine whether the product inside the parcel is damaged.
- Inspect parcels during delivery to the customer.
- Determine who caused the damage.
- Automatically approve or reject customer refunds or returns.
- Replace human inspection when further investigation is required.

## 8. Business Benefits

The proposed system could provide the following benefits to Takealot:

- Detect damaged parcels before they leave the warehouse.
- Improve the quality-control process during parcel dispatch.
- Provide evidence of the parcel's condition before dispatch.
- Support faster and more informed investigations of damage-related complaints.
- Help reduce unnecessary returns, refunds and replacement costs.
- Improve accountability and consistency in parcel inspection.
- Create a foundation for future automation of parcel quality control.



