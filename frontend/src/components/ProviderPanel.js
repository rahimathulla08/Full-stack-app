import { useSelector, useDispatch } from 'react-redux';
import { setCurrentSession } from '../../store/slices/sessionsSlice';

const ProviderPanel = () => {
  const dispatch = useDispatch();
  const currentSession = useSelector((state) => state.sessions.currentSession);
  const providers = ['OpenAI', 'Claude', 'Gemini'];

  const handleChange = (e) => {
    if (!currentSession) return;

    const updatedSession = { ...currentSession, provider: e.target.value };
    dispatch(setCurrentSession(updatedSession));
  };

  return (
    <div style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
      <span>Provider: </span>
      <select value={currentSession?.provider || ''} onChange={handleChange}>
        <option value="">Select Provider</option>
        {providers.map((p) => (
          <option key={p} value={p}>{p}</option>
        ))}
      </select>
    </div>
  );
};

export default ProviderPanel;