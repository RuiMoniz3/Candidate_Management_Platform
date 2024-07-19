import React, { useState } from 'react';
import './styles/CandidaturasPopup.css';

const CandidaturasPopup = ({ applications, onClose, onStatusUpdate }) => {
    const [statusMap, setStatusMap] = useState({});
    const [filterTitle, setFilterTitle] = useState('');

    const handleStatusChange = async (event, id) => {
        const newStatus = event.target.value;
        setStatusMap({
            ...statusMap,
            [id]: newStatus,
        });
        await handleSubmit(id, newStatus);
    };

    const handleSubmit = async (id, status) => {
        if (!status) return;
        await onStatusUpdate(id, status);
    };

    const filteredApplications = applications.filter(application =>
        application.vaga.titulo.toLowerCase().includes(filterTitle.toLowerCase())
    );

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <button className="popup-close" onClick={onClose}>✕</button>
                <h2>Aplicações</h2>
                <input
                    type="text"
                    placeholder="Pesquisar"
                    value={filterTitle}
                    onChange={(e) => setFilterTitle(e.target.value)}
                    className="filter-input"
                />
                <table className="table">
                    <thead>
                        <tr>
                            <th>Título</th>
                            <th>Descrição</th>
                            <th>Data de Publicação</th>
                            <th>Cliente</th>
                            <th>Recrutador</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredApplications.map(({ id, vaga, estado }) => (
                            <tr key={id}>
                                <td>{vaga.titulo}</td>
                                <td>{vaga.descricao}</td>
                                <td>{vaga.data_publicacao}</td>
                                <td>{vaga.cliente.nome}</td>
                                <td>{vaga.recrutador.nome}</td>
                                <td>
                                    <select
                                        value={statusMap[id] || estado}
                                        onChange={(event) => handleStatusChange(event, id)}
                                    >
                                        <option value="em_processo">Em Processo</option>
                                        <option value="desqualificado">Desqualificado</option>
                                        <option value="desistiu">Desistiu</option>
                                        <option value="contratado">Contratado</option>
                                    </select>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default CandidaturasPopup;
