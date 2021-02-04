import './styles.css'
import { useHistory } from "react-router-dom"

function Home() {

  const history = useHistory();

  const handlerTipoJogo = (tela: string) => {
    const salaId = tela
    history.push(`/room/${salaId}`)
  }

  return (
    <div className="home">
        <div>
            <h1>Battlefield</h1>
            <input type="text" placeholder="Insert your nickname" />
            <button onClick={() => handlerTipoJogo('privada')}>Partida privada</button>
            <button onClick={() => handlerTipoJogo('procurar')}>Procurar jogador</button>
        </div>
    </div>
  );
}

export default Home;