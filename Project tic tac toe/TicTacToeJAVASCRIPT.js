window.addEventListener('DOMContentLoaded', () => {
    const tiles = Array.from(document.querySelectorAll('.tile'));
    const playerDisplay = document.querySelector('.display-player');
    const resetButton = document.querySelector('#reset');
    const announcer = document.querySelector('.announcer');
    let previousWinner = null;

    let board = ['', '', '', '', '', '', '', '', ''];
    let huidige_speler = 'X';
    let isGameActive = true;

    const SPELER_X_GEWONNEN = 'PLAYERX_WON';
    const SPELER_O_GEWONNEN = 'PLAYERO_WON';
    const TIE = 'TIE';


    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    function handleResultValidation() {
        let Ronde_gewonnen = false;
        for (let i = 0; i <= 7; i++) {
            const winCondition = winningConditions[i];
            const a = board[winCondition[0]];
            const b = board[winCondition[1]];
            const c = board[winCondition[2]];
            if (a === '' || b === '' || c === '') {
                continue;
            }
            if (a === b && b === c) {
                Ronde_gewonnen = true;
                break;
            }
        }

    if (Ronde_gewonnen) {
            announce(huidige_speler === 'X' ? SPELER_X_GEWONNEN : SPELER_O_GEWONNEN);
            isGameActive = false;
            return;
        }

    if (!board.includes(''))
        announce(TIE);
    }

    const announce = (type) => {
        switch(type){
            case SPELER_O_GEWONNEN:
                announcer.innerHTML = 'Player <span class="playerO">O</span> Won';
                break;
            case SPELER_X_GEWONNEN:
                announcer.innerHTML = 'Player <span class="playerX">X</span> Won';
                break;
            case TIE:
                announcer.innerText = 'Tie';
        }
        announcer.classList.remove('hide');
    };

    const isValidAction = (tile) => {
        if (tile.innerText === 'X' || tile.innerText === 'O'){
            return false;
        }

        return true;
    };

    const updateBoard =  (index) => {
        board[index] = huidige_speler;
    }

    const changePlayer = () => {
        playerDisplay.classList.remove(`player${huidige_speler}`);
        huidige_speler = huidige_speler === 'X' ? 'O' : 'X';
        playerDisplay.innerText = huidige_speler;
        playerDisplay.classList.add(`player${huidige_speler}`);
    }

    const userAction = (tile, index) => {
        if(isValidAction(tile) && isGameActive) {
            tile.innerText = huidige_speler;
            tile.classList.add(`player${huidige_speler}`);
            updateBoard(index);
            handleResultValidation();
            changePlayer();
        }
    }
    
    const resetBoard = () => {
        board = ['', '', '', '', '', '', '', '', ''];
        isGameActive = true;
        announcer.classList.add('hide');

        if (huidige_speler === 'O') {
            changePlayer();
        }

        tiles.forEach(tile => {
            tile.innerText = '';
            tile.classList.remove('playerX');
            tile.classList.remove('playerO');
        });
    }

    tiles.forEach( (tile, index) => {
        tile.addEventListener('click', () => userAction(tile, index));
    });

    resetButton.addEventListener('click', resetBoard);
});


if (winningCombination) {
    previousWinner = currentPlayer;
    document.getElementById("previous-winner").textContent = previousWinner + " heeft gewonnen";

}