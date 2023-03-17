import DoneAllIcon from '@mui/icons-material/DoneAll';
import SendIcon from '@mui/icons-material/Send';
import { Chip, IconButton, InputBase, Paper } from '@mui/material';
import axios from 'axios';
import { useState } from 'react';

function App() {
  const [res, setRes] = useState("")
  const [input_text, setIT] = useState("")
  const labels = [
    "Anger",
    "Disgust",
    "Enjoyment",
    "Fear",
    "Other",
    "Sadness",
    "Surprise",
  ]

  const handleSubmit = async (e) => {
    console.log(input_text);
    const article = { title: 'Axios POST Request Example' };
    let temp = await axios.post('https://reqres.in/api/articles', article).then(data => data)
    console.log(temp.data);
    // setRes()
  }
  const handleChange = (e) => {
    console.log(e.target.value);
    setIT(e.target.value);
  }

  return (
    <>
      <Paper
        component="form"
        sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: "100%", height: "fit-content", background: "#ddd" }}
      >
        <InputBase
          rows={20}
          multiline
          placeholder="Input"
          sx={{ ml: 1, flex: 1 }}
          onChange={handleChange}
          inputProps={{ 'aria-label': 'search', spellCheck: 'false' }}
        />
        <IconButton type="button" sx={{ p: '10px' }} aria-label="search" onClick={handleSubmit}>
          <SendIcon color='info' />
        </IconButton>
      </Paper>
      {labels.map((label, i) => <Chip label={label} key={i}
        variant={res === label ? "filled" : "outlined"} color="success" sx={{
          fontSize: 40, height: "auto",
          borderRadius: "9999px",
          marginTop: 10,
          marginLeft: 5,
        }} deleteIcon={<DoneAllIcon />} onDelete={res === label ? () => { } : null} />)}
    </>
  );
}

export default App;
