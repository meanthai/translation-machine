import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { translatePrompt } from "@/types";
import { useState } from "react";
import { translateResponse } from "@/types";
import { TbExchange } from "react-icons/tb";


type Props = {
    onSave: (inputPrompt: translatePrompt) => Promise<translateResponse>,
}

let defaultLang = "en_to_vn";

const TranslateInput = ({onSave}: Props) => {
    const [inputValue, setInputValue] = useState("");

    const [outputValue, setOutputValue] = useState("output");

    let [languageMode, setLanguageMode] = useState(defaultLang);

    const changeInput = (e: React.ChangeEvent<HTMLInputElement> ) => {
        setInputValue(e.target.value);
        if(e.target.value === "") {
            setOutputValue("");
        }
    }

    const onChangeLanguage = () => {
        languageMode = (languageMode === "vn_to_en" ? "en_to_vn" : "vn_to_en");
        setLanguageMode(languageMode);
    }

    const onTranslate = async () => {
        if (inputValue.trim() === "") {
            alert("Please enter a prompt to translate!");
            return;
        }

        const inputPrompt: translatePrompt = {
            lang: languageMode, 
            prompt: inputValue,
        };

        const translatedOutput = await onSave(inputPrompt);
        console.log(translatedOutput);

        setOutputValue(translatedOutput.response);

        // I want to asign the translated output to the input that has the id "output" here 
    }

    return (
        <div className="gap-10 flex flex-col p-10 items-center justify-between">
            <h1 className="text-3xl font-bold">Transformer with Attention Mechanism - Translation Machine</h1>
            
            <div className="flex flex-col gap-5 justify-between items-center w-[90%] h-[80%] p-20 border-4 border-grey-300 rounded-lg">
                <Button className="items-center justify-items-center bg-red-500" id="changeLanguage" onClick={onChangeLanguage} value={languageMode}>
                    <TbExchange/> {(languageMode === "en_to_vn" ? "English to Vietnamese" : "Vietnamese to English")}
                </Button>
                
                <Input className="border-black-500 p-5 font-bold text-2xl" id="input" onChange={changeInput} value={inputValue} placeholder="Enter the prompt you want to translate"/>
                
                <Input className="border-red-500 p-5 font-bold text-2xl" id="output" value={outputValue} disabled placeholder="Translated text here!"/>

                <Button id="translateBtn font-bold" className="bg-yellow-500 items-center justify-items-center" type="submit" onClick={onTranslate}>Translate</Button>
            </div>
        </div>
    )
}

export default TranslateInput;