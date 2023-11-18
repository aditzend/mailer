import pandas as pd
import requests
import logging

logger = logging.getLogger("uvicorn")


async def transform_and_save_xlsx(file_name: str):
    # Step 1: Read the .xlsx file
    try:
        df = pd.read_excel(f"../data/{file_name}.xlsx")
    except Exception as e:
        return f"Error reading the Excel file: {e}"

    # Step 2: Extract 'Numero de Whatsapp' column
    if "Número de WhatsApp 📞" not in df.columns:
        return "Error: 'Número de WhatsApp 📞' column not found in the file"

    # Step 3: Call the API for each value and store the result in a new column
    normalized_numbers = []
    for number in df["Número de WhatsApp 📞"]:
        api_url = "https://lab.saia.ar/lab/entities/parse"
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data = {"user_input": str(number), "entities": "NumeroCelular"}
        logger.debug(f"Calling API with data: {data}")

        try:
            response = requests.post(api_url, json=data, headers=headers)
            if response.status_code == 200 and "NumeroCelular" in response.json():
                normalized_number = response.json()["NumeroCelular"]
                if len(normalized_number) != 14:
                    normalized_numbers.append("E")
                    logger.info(
                        f"Normalized number does not meet the criteria: {normalized_number}"
                    )
                else:
                    # trim the + sign at the beginning
                    normalized_number = normalized_number[1:]
                    normalized_numbers.append(normalized_number)
                    logger.info(f"Normalized number: {normalized_number}")
            else:
                normalized_numbers.append("API call failed or no normalized number")
        except Exception as e:
            normalized_numbers.append(f"Error: {str(e)}")
            logger.error(f"Error: {str(e)}")

    # Add the new column to the DataFrame
    df["NumeroNormalizado"] = normalized_numbers

    # Step 4: Export the DataFrame to a new Excel file
    output_file = f"../data/{file_name}_normalized.xlsx"
    try:
        df.to_excel(output_file, index=False)
        return f"File successfully saved as {output_file}"
    except Exception as e:
        return f"Error saving the Excel file: {e}"


# Example usage:
# result = transform_and_save_xlsx("path_to_your_file.xlsx", "output_file.xlsx")
# print(result)
