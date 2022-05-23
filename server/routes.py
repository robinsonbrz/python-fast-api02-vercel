from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.model import NoteSchema

router = APIRouter()

notes = {
    "1": {
        "title": "Primeira anotação.",
        "content": "Esta é minha primeira anotação"
    },
    "2": {
        "title": "Segunda anotação.",
        "content": "Fast API é rápido e completo."
    }
}


@router.get("/")
def get_notes() -> dict:
    '''
    Get sem parâmetros retorna todas as notas
    '''
    return {
        "data": notes
    }


@router.get("/{id}")
async def get_note(id: str) -> dict:
    '''
    Get com parâmetro ID retorna nota com o ID solicitado
    '''
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            return {
                "data": notes[note]
            }

    return {
        "Error": "Invalid ID"
    }


@router.post("/")
def add_note(note: NoteSchema = Body(...)) -> dict:
    '''
    Post Insere nota. Necessário preenchimento do corpo
    '''
    notes[str(len(notes) + 31)] = note.dict()

    return {
        "message": "Note added successfully"
    }
#


@router.put("/{id}")
def update_note(id: str, note: NoteSchema):
    '''
    Put edita nota com o parâmetro ID solicitado. \nNecessário preenchimento do corpo com a nova nota, e o ID da Nota a ser atualizada.
    '''
    stored_note = notes[id]
    if stored_note:
        stored_note_model = NoteSchema(**stored_note)
        update_data = note.dict(exclude_unset=True)
        updated_note = stored_note_model.copy(update=update_data)
        notes[id] = jsonable_encoder(updated_note)
        return {
            "message": "Note updated successfully"
        }
    return {
        "error": "No such note exist"
    }


@router.delete("/{id}")
def delete_note(id: str) -> dict:
    '''
    Delete com parâmetro ID deleta nota com o ID solicitado
    '''    
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            del notes[note]
            return {
                "message": "Note deleted"
            }

    return {
        "error": "Note with {} doesn't exist".format(id)
    }
