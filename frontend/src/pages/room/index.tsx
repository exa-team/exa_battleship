import { useParams } from "react-router-dom";
interface Params {
    salaId: string
}

function Room() {
    let { salaId } = useParams<Params>();

    if (salaId === 'private') {
        return <p>private</p>
    } else if (salaId === 'public') {
        return <p>public</p>
    } else {
        return <p>error</p>
    }

    // return <p>deuboa:{ salaId }</p>
}

export default Room;