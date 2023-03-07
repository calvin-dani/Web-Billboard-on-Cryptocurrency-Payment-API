import logo from './message.svg';
import donateicon from './donate.svg'
import './App.css';
import ScaleText from "react-scale-text";
import { useEffect, useState } from 'react';

function App() {
  //State Hooks to update the message and author 
  const [message, setMessage] = useState("Fetching messages.. Please wait!!")
  const [author, setAuthor] = useState("Developer")
  const [donation_min_value,setDonationValue] = useState(0)

  useEffect(() => {
    //Get the message of the highest donor
    let get_message = () => {
      fetch("http://localhost:5005/get_message", {
        method: "GET",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        }
      })
      .then(response => response.json())
      .then(data =>{
        console.log(data);
        setMessage(data["message"]);
        setAuthor(data["name"]);
        setDonationValue(data['value'])
      } ).catch(err => console.error(err)); // your GET request URL
    };

   
    //Ping the analytic server for the latest message of the highest donor
    let interval = setInterval(get_message, 30000); // set the interval time in milliseconds

    return () => clearInterval(interval); // clean up the interval when unmounting
  }, []);

 
  return (
    <div className="App">
      <header className="App-header">
        <div className="title">
          <ScaleText minFontSize={30}>Blockonomics Billboard</ScaleText>
        </div>
        <div>
          <img src={logo} className="App-logo" alt="logo" />
        </div>
        <div className='message-space'>
          <ScaleText maxFontSize={55}>{message} </ScaleText>
          <ScaleText maxFontSize={25}>by {author}</ScaleText>
        </div>
        <div className="donation">
          <ScaleText maxFontSize={15}>Share ypu message for 0.00{donation_min_value} BTC Click Below!!</ScaleText>
          {/*Contains the Blockonomics payment button */}
          <a href="#" class="blockoPayBtn" data-toggle="modal" data-uid="78103a0e3ac54e3a"><img src={donateicon} className="Donate-logo" alt="donate" /></a>
        </div>

      </header>
    </div>
  );
}

export default App;