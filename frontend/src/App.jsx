import { useEffect, useState } from "react";

function App(){
  const [mentions, setMentions] = useState([]);
  useEffect(() => {
    fetch("/api/mentions")
      .then(r=>r.json())
      .then(d=> setMentions(d.mentions || []))
      .catch(e => console.error(e));
  }, []);
  return (
    <div style={{padding:24, fontFamily:"Inter, sans-serif"}}>
      <h1>BuzzGuard — Live Mentions</h1>
      <ul>
        {mentions.map(m => (
          <li key={m.mention_id} style={{marginBottom:12}}>
            <div><b>{m.source}</b> • {new Date(m.collected_at).toLocaleString()}</div>
            <div>{m.text?.slice(0,200)}{m.text?.length>200?"...":""}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
