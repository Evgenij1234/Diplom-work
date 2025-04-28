import React from "react";
import ParserSection from "./Text";
import { useNavigate } from 'react-router-dom';

function Start() {
  const navigate = useNavigate();
  return (
    <div className="Start">
      <div className="Start-title">
        <div className="Start-title-left">
          <span className="Start-title-left-span">
            Ваши конкуренты скрывают свои секреты? Раскройте их и используйте в
            своих интересах.
          </span>
          <button onClick={() => navigate('/Work')} className="Start-title-left-button">
            Начать
          </button>
        </div>
        <div className="Start-title-right">
          <span className="Start-title-right-span">Скрапинг не запрещён - отставание запрещено! Получайте конкурентные преимущества уже сегодня</span>
          <button onClick={() => navigate('/Work/manual')} className="Start-title-right-button">
            Руководство
          </button>
        </div>
      </div>
      <div className="Start-text">
        <ParserSection></ParserSection>
      </div>
    </div>
  );
}

export default Start;
