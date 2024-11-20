import React from 'react';
import { Tabs, Tab, Box } from '@mui/material';

const OutputTabs = ({ explanation, debuggingTips, challenge }) => {
  const [selectedTab, setSelectedTab] = React.useState(0);

  const handleChange = (event, newValue) => {
    setSelectedTab(newValue);
  };

  return (
    <Box>
      <Tabs value={selectedTab} onChange={handleChange}>
        <Tab label="Explanations" />
        <Tab label="Debugging Tips" />
        <Tab label="Challenges" />
      </Tabs>
      <Box sx={{ padding: 2 }}>
        {selectedTab === 0 && <pre>{explanation || 'No explanation yet.'}</pre>}
        {selectedTab === 1 && <pre>{debuggingTips || 'No tips yet.'}</pre>}
        {selectedTab === 2 && <pre>{challenge || 'No challenge yet.'}</pre>}
      </Box>
    </Box>
  );
};

export default OutputTabs;
