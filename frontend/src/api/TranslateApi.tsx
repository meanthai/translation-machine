import { translatePrompt, translateResponse } from "@/types"
import { useMutation } from "@tanstack/react-query"

const backend_api = import.meta.env.VITE_BACKEND_API

type Props = {
    lang: string,
    prompt: string
}

export const useTranslate = () => {
    const getTranslatePrompt = async (inputData: translatePrompt): Promise<translateResponse> => {
        console.log("Input data received:", inputData);

        console.log("backend api:", backend_api);

        const response = await fetch(`${backend_api}/api/translate`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(inputData),
        });

        if(!response.ok){
            throw new Error("cannot send api request to the backend!");
        }

        return await response.json();
    }

    return {
        getTranslatePrompt
    }

}