import React, { useEffect, useState } from "react";
import "./style/App.scss";

function Notification({ message }) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (message) {
      setVisible(true);
      const timer = setTimeout(() => setVisible(false), 1500);
      return () => clearTimeout(timer);
    }
  }, [message]);

  if (!visible) return null;

  return (
    <div className="Notification">
        <div className="Notification-text">
        {message}
        </div>
    </div>
  );
}

export default Notification;