# Pantun Generator App

This is a simple Pantun Generator app, built with **Streamlit**, that helps users generate Malay **pantun** based on the first line they provide. The app uses a fine-tuned GPT-4o model trained on a dataset of 3000 **pantun**. 

Developed by **Abu Huzaifah Bidin**, this app leverages the OpenAI API and is fully interactive, allowing users to input a phrase and receive a generated pantun in real-time.

## Features

- **Generate Pantun**: Users input the first line of a **pantun** and the model generates a matching continuation.
- **Pantun Regeneration**: Users can regenerate the pantun up to 10 times to get different results.
- **Malay Language Only**: The app supports and generates only Malay **pantun**.
- **Streamlit-Based**: The app is built using Streamlit for a smooth user interface.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, OpenAI GPT-4o fine-tuned model
- **API Integration**: OpenAI API for generating **pantun**

## Installation

To run this app locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pantun-generator-app.git
    cd pantun-generator-app
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for OpenAI API key:

    Create a `.env` file in the root of your project and add your OpenAI API key:

    ```
    OPENAI_API_KEY=your-api-key-here
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Open your browser and visit:

    ```
    http://localhost:8501
    ```

## Usage

- **Input**: Type the first line of your pantun in the input box.
- **Generate Pantun**: Click the "Hasilkan Pantun" button to generate a full four-line **pantun**.
- **Regenerate**: Click "Hasilkan semula pantun" to regenerate a new **pantun** based on the same input (up to 10 times).
- **Pantun Reset**: After 10 generations, the pantun will be reset, and you can start with a fresh input.

## Example

1. Input: 
   - **Sila masukkan baris pertama pantun:** *"Makan nasi berulamkan ikan"*

2. Output:
   - Makan nasi berulamkan ikan,  
     Air jernih mengalir laju,  
     Budi baik sentiasa dikenang,  
     Hingga akhir hidupku.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Author

Developed by **Abu Huzaifah Bidin**.  
Feel free to contact me for any questions or collaboration ideas.
