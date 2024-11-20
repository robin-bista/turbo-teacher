import React, { useState } from 'react';
import CodeEditor from './components/CodeEditor';
import OutputTabs from './components/OutputTabs';
import Header from './components/Header';
import './App.css';

const App = () => {
  // State variables to manage explanation, debugging tips, and challenges
  const [explanation, setExplanation] = useState('');
  const [debuggingTips, setDebuggingTips] = useState('');
  const [challenge, setChallenge] = useState('');

  const handleSubmit = async (code) => {
    try {
      // Send code to the Flask backend
      const response = await fetch('http://localhost:5000/api/parse-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code }), // Send the code as JSON
      });

      const data = await response.json();
      console.log('Backend Response:', data); // Debug log

      // Set state with the data received from the backend
      setExplanation(data.explanation || 'No explanation available.');
      setDebuggingTips(data.debuggingTips || 'No debugging tips available.');
      setChallenge(data.challenge || 'No challenge available.');
    } catch (error) {
      console.error('Error:', error); // Log any errors
      setExplanation('Error: Unable to fetch explanation.');
      setDebuggingTips('Error: Unable to fetch debugging tips.');
      setChallenge('Error: Unable to fetch challenges.');
    }
  };

  return (
    <div className="App">
      <Header />
      {/* Code editor for user to input code */}
      <CodeEditor onSubmit={handleSubmit} />
      {/* Tabs for displaying output */}
      <OutputTabs
        explanation={explanation}
        debuggingTips={debuggingTips}
        challenge={challenge}
      />
    </div>
  );
};

export default App;
