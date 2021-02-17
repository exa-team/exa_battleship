import "./styles.css";
import { useHistory } from "react-router-dom";
import axios from "axios";
import { useMemo, useState } from "react";

const Gear = () => {
  return (
    <img
      className="gear"
      src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Gear_icon_svg.svg"
      alt="gear"
    />
  );
};

interface BotaoProps {
  onClique: () => void;
  loading: boolean;
  textoDefault: string;
  textoLoading: string;
  disabled: boolean;
}

const Botao = ({ onClique, loading, textoDefault, textoLoading, disabled }: BotaoProps) => {
  return (
    <button onClick={onClique} disabled={disabled}>
      {!loading && textoDefault}
      {loading && (
        <>
          <span>{textoLoading}</span>
          <Gear />
        </>
      )}
    </button>
  );
};

const ERROR_NICK_MESSAGE = "Nickname it's necessary.";

interface AlertProps {
  message: string;
}

const Alert = ({ message }: AlertProps) => {
  return (
    <div className="alert">
      <span>{message}</span>
    </div>
  );
};

function Home() {
  const [name, setName] = useState("");
  const history = useHistory();
  const [fetching, setFetching] = useState<{ [key: string]: boolean }>({});
  const [roomId, setRoomId] = useState("");
  const [errorList, setErrorList] = useState<string[]>([]);

  const handlerTipoJogo = (tela: string) => {
    // const salaId = tela

    if (!name) {
      setErrorList([ERROR_NICK_MESSAGE]);
      return;
    }

    // verifica o tipo de pesquisa
    // let fetching2 = fetching
    // fetching2[tela] = true
    // setFetching(fetching2);
    setFetching({ ...fetching, [tela]: true });

    axios
      .post("http://localhost:8000/room", {
        nickname: name,
      })
      .then((response) => {
        setRoomId(response.data.id);
        history.push(`/room/${response.data.id}`);
      })
      .catch((error) => {
        setErrorList(["Something went wrong :("]);
      });
  };

  const errorNick = useMemo(
    () => errorList.find((errorMessage) => errorMessage === ERROR_NICK_MESSAGE),
    [errorList]
  );

  return (
    <div className="home">
      <div>
        {errorList.map((item) => (
          <Alert message={item} key={item} />
        ))}
        <h1>Exa Battleship</h1>
        <input
          type="text"
          className={errorNick ? "erro" : ""}
          placeholder="Insert your nickname"
          onChange={(event) => {
            setName(event.target.value);
            setErrorList([]);
          }}
        />

        <Botao
          onClique={() => handlerTipoJogo("private")}
          loading={fetching["private"] && !roomId}
          textoDefault="Private game"
          textoLoading="Creating game"
          disabled={Object.keys(fetching).length !== 0}
        />
        <Botao
          onClique={() => handlerTipoJogo("public")}
          loading={fetching["public"] && !roomId}
          textoDefault="Public game"
          textoLoading="Searching game"
          disabled={Object.keys(fetching).length !== 0}
        />
      </div>
    </div>
  );
}

export default Home;
