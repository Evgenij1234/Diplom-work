import React, { useEffect, useState } from "react";
import "./style/App.scss";

function Notification({ message, id }) {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    setVisible(true);
    const timer = setTimeout(() => setVisible(false), 1500);
    return () => clearTimeout(timer);
  }, [message, id]); // Добавьте id в зависимости

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