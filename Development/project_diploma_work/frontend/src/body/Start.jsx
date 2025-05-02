import React from "react";
import ParserSection from "./Text";
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { showAuthForm } from '../redux/counter/authSlice';

function Start() {
  const navigate = useNavigate();
  const { isAuthenticated } = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  function handleWorkNavigate() {
    if (isAuthenticated) {
      navigate('/Work');
    }
    else{
      dispatch(showAuthForm());
    }
  }

  function handleManualNavigate() {
    if (isAuthenticated) {
      navigate('/Work/manual');
    }
    else{
      dispatch(showAuthForm());
    }
  }

  function renderStartButton() {
    return (
      <button 
        onClick={handleWorkNavigate} 
        className={`Start-title-left-button`}
      >
        Начать
      </button>
    );
  }

  function renderManualButton() {
    return (
      <button 
        onClick={handleManualNavigate} 
        className={`Start-title-right-button`}
      >
        Руководство
      </button>
    );
  }

  return (
    <div className="Start">
      <div className="Start-title">
        <div className="Start-title-left">
          <span className="Start-title-left-span">
            Ваши конкуренты скрывают свои секреты? Раскройте их и используйте в
            своих интересах.
          </span>
          {renderStartButton()}
        </div>
        <div className="Start-title-right">
          <span className="Start-title-right-span">
            Скрапинг не запрещён - отставание запрещено! Получайте конкурентные преимущества уже сегодня
          </span>
          {renderManualButton()}
        </div>
      </div>
      <div className="Start-text">
        <ParserSection />
      </div>
    </div>
  );
}

export default Start;