import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Input } from './components/ui/input'
import { createRoot } from 'react-dom/client'
import TranslateInput from './components/TranslateInput'
import { useTranslate } from './api/TranslateApi'


const App = () => {

  const {getTranslatePrompt} = useTranslate();

  return (
    <div className='flex flex-col items-center h-screen w-full justify-items-center align-middle'>
      <TranslateInput onSave={getTranslatePrompt} />
    </div>
  )
}

export default App
