import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles/CandidatosLista.css';
import CandidaturasPopup from './CandidaturasPopup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye } from '@fortawesome/free-solid-svg-icons';

const CandidatosLista = () => {
    const [candidates, setCandidates] = useState([]);
    const [filteredCandidates, setFilteredCandidates] = useState([]);
    const [selectedCandidate, setSelectedCandidate] = useState(null);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [filterName, setFilterName] = useState('');

    useEffect(() => {
        const fetchCandidates = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/candidatos/');
                setCandidates(response.data);
                setFilteredCandidates(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchCandidates();
    }, []);

    useEffect(() => {
        const filterCandidates = () => {
            const filtered = candidates.filter(candidate =>
                candidate.nome.toLowerCase().includes(filterName.toLowerCase())
            );
            setFilteredCandidates(filtered);
        };

        filterCandidates();
    }, [filterName, candidates]);

    const handleButtonClick = async (candidateId) => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/candidaturas/?candidato=${candidateId}`);
            setSelectedCandidate({ id: candidateId, applications: response.data });
            setIsPopupOpen(true);
        } catch (error) {
            console.error('Error fetching applications:', error);
        }
    };

    const closePopup = () => {
        setIsPopupOpen(false);
        setSelectedCandidate(null);
    };

    const updateStatus = async (applicationId, status) => {
        try {
            await axios.post(`http://127.0.0.1:8000/api/candidaturas/${applicationId}/update_status/`, { status });
            // Fetch updated applications
            const response = await axios.get(`http://127.0.0.1:8000/api/candidaturas/?candidato=${selectedCandidate.id}`);
            setSelectedCandidate({ id: selectedCandidate.id, applications: response.data });
        } catch (error) {
            console.error('Error updating status:', error);
        }
    };

    return (
        <div className="table-container">
            <h1 className="table-caption">Candidatos</h1>
            <input
                type="text"
                placeholder="Pesquisar"
                value={filterName}
                onChange={(e) => setFilterName(e.target.value)}
                className="filter-input"
            />
            <table className="table">
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Email</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {filteredCandidates.map(({ id, nome, email }) => (
                        <tr key={id}>
                            <td>{nome}</td>
                            <td>{email}</td>
                            <td className="button-column">
                                <button className="icon-button" onClick={() => handleButtonClick(id)}>
                                    <FontAwesomeIcon icon={faEye} />
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {isPopupOpen && selectedCandidate && (
                <CandidaturasPopup
                    applications={selectedCandidate.applications}
                    onClose={closePopup}
                    onStatusUpdate={updateStatus}
                />
            )}
        </div>
    );
};

export default CandidatosLista;
