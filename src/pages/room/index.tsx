import { useParams } from "react-router-dom";
interface Params {
    salaId: string
}

function Room() {
    let { salaId } = useParams<Params>();

    if (salaId === 'privada') {
        return <p>privada</p>
    } else if (salaId === 'procurar') {
        return <p>procurar</p>
    } else {
        return <p>NADA PRA NAO DAR ERRO</p>
    }

    // return <p>deuboa:{ salaId }</p>
}

export default Room;