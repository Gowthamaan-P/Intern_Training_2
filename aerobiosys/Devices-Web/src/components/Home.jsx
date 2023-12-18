import React, { useEffect } from 'react';
import './Home.css';
const Home = () => {
  useEffect(() => {
    const text = document.querySelector('.second-text');

    const textLoad = () => {
      setTimeout(() => {
        text.textContent = ' Aerobiosys Innovations';
      }, 0);
      setTimeout(() => {
        text.textContent = " Manufacturing India's Best Medical ICU Ventilators";
      }, 4500);
      setTimeout(() => {
        text.textContent = ' changing the way you receive healthcare';
      }, 9000);
	};
    textLoad();
	setInterval(textLoad,13500)
  }, []);

  return (
    <div className="container-home">
      <span className="text first-text">Welcome, We are</span>
      <span className="text second-text"></span>
    </div>
  );
};

export default Home;
