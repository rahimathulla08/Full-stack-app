import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addMessage } from '../../store/slices/messagesSlice';

const Composer = () => {
  const [message, setMessage] = useState('');
  const dispatch = useDispatch();
  const currentSession = useSelector((state) => state.sessions.currentSession);

  const handleSend = () => {
    if (!message.trim() || !currentSession) return;

    const newMessage = {
      id: Date.now(),
      sessionId: currentSession.id,
      role: 'user',
      content: message,
    };

    dispatch(addMessage(newMessage));
    setMessage('');
  };

  return (
    <div style={{ padding: '10px', borderTop: '1px solid #ccc' }}>
      <textarea
        rows="2"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
        style={{ width: '100%' }}
      />
      <button onClick={handleSend} style={{ marginTop: '5px' }}>Send</button>
    </div>
  );
};

export default Composer;