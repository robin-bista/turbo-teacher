import React, { useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';

const CodeEditor = ({ onSubmit }) => {
  const [code, setCode] = useState('');

  return (
    <div>
      <h3>Paste Your Code Here</h3>
      <CodeMirror
        value={code}
        height="200px"
        extensions={[python()]}
        onChange={(value) => setCode(value)}
        options={{
          theme: 'light', // Adjust the theme as needed
        }}
      />
      <button onClick={() => onSubmit(code)} className="action-button">
        Submit Code
      </button>
    </div>
  );
};

export default CodeEditor;
