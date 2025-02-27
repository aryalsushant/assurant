
# Home Insurance Fraud Detection System

## Project Overview
This project is a multimodal home insurance fraud detection system designed to identify potential fraudulent claims based on the analysis of insurance claims data and the images provided. The system uses a convolutional neural network (CNN) model trained on a labeled dataset of manipulated and original images to detect image manipulation. Additionally, the system leverages AI (via OpenAI's GPT) to analyze claim data for anomalies and assign a legitimacy rating.

The system takes the Claim ID as input and performs the following tasks:
1. Analyzes the claim information for anomalies.
2. Analyzes the provided image to determine whether it has been manipulated.
3. Assigns a legitimacy rating based on both the claim and image analysis.

<img width="852" alt="Screenshot 2025-02-27 at 12 01 29 PM" src="https://github.com/user-attachments/assets/22b58d63-90e1-4137-9a00-f6cfd8929b07" />


## Features
- **Image Manipulation Detection**: A CNN model trained to distinguish between manipulated and original images.
- **Claim Analysis**: AI analysis of the claim based on its content, evaluating the legitimacy based on historical data and relevant factors.
- **Legitimacy Rating**: An AI-powered rating of the claim's legitimacy from 0 to 5, considering both image manipulation and claim anomalies.

## Installation

### Prerequisites
- Python 3.x
- TensorFlow (for image analysis)
- OpenAI API Key (for claim analysis)
- Required Python libraries (`dotenv`, `numpy`, `tensorflow`, `openai`)

### Setup
1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .env
   source .env/bin/activate  # For Linux/macOS
   .env\Scripts\activate     # For Windows
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API Key:
   ```
   OPENAI_API_KEY=<your_api_key>
   ```

## Usage

1. **Train the Model**: Before using the system, make sure to train the CNN model using the dataset:
   - The model is trained on labeled images (original and manipulated) stored in the `data/TRAINING_CG-1050` directory for training and `data/VALIDATION_CG-1050` for validation.
   - The training process will save the trained model as `models/image_model.h5`.

   You can train the model by running:
   ```bash
   python src/train_image_model.py
   ```

2. **Run the Main Program**:
   After training the model, you can use the system to analyze a claim and its corresponding image. Run the following command:
   ```bash
   python src/main.py
   ```

   The system will prompt you for a Claim ID, fetch the corresponding claim details and image, and analyze both to provide a legitimacy rating.

3. **Interaction with the AI Agent**:
   After receiving the legitimacy rating, you can continue interacting with the AI agent by asking questions related to the claim or insurance process. Type `exit` to quit the session.

## File Structure
```
.
├── claims/
│   └── images/
├── data/
│   ├── TRAINING_CG-1050/
│   └── VALIDATION_CG-1050/
├── models/
│   └── image_model.h5
├── src/
│   ├── claims_analysis.py
│   ├── image_analysis.py
│   ├── main.py
│   ├── train_image_model.py
│   └── utils.py
├── .env
├── .gitignore
└── requirements.txt
```

## Contributing
If you would like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them with clear and concise messages.
5. Push your changes to your forked repository.
6. Create a pull request to the main repository.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [OpenAI](https://openai.com/) for providing the GPT-4 model to analyze claims.
- [TensorFlow](https://www.tensorflow.org/) for the CNN model implementation.
- Dataset provided by [CG-1050](https://example.com) for training and validation.
