<?php

namespace App\Infrastructure\Persistence\##TABLENAMECAP##;

##USECLAUSES##

use PDO;

class DB##TABLENAMECAP##Repository implements ##TABLENAMECAP##Repository
{
    /**
     * @var PDO
     */
    private PDO $connection;

    /**
     * @param PDO $connection
     */
    public function __construct(PDO $connection)
    {
        $this->connection = $connection;
    }

    /**
     * {@inheritdoc}
     */
    public function getAll(): array
    {
        $retData = array();
        $query = "SELECT ##FIELDSLIST## FROM ##TABLENAME##";
        $stmt = $this->connection->prepare($query);
        $stmt->execute();
        if ($stmt->rowCount() > 0) {
            while ($row = $stmt->fetch()) {
                $rec = new ##TABLENAMECAP##(##FIELDSROW##);
                $retData[] = $rec;
            }
        }
        return $retData;
    }

    /**
     * {@inheritdoc}
     */
    public function get(##KEYPARAMS##): ##TABLENAMECAP##
    {
        $retData = null;
        $query = "SELECT ##FIELDSLIST## FROM ##TABLENAME## WHERE ##WHEREKEY##";
        $stmt = $this->connection->prepare($query);
        $stmt->execute(array(##GETARRAY##));
        if ($stmt->rowCount() > 0) {
            $row = $stmt->fetch();
            $retData = new ##TABLENAMECAP##(##FIELDSROW##);
        } else {
            throw new ##TABLENAMECAP##NotFoundException();
        }
        return $retData;
    }
    /**
     * {@inheritdoc}
     */
    public function getSubset(string $filtro, string $sortBy, int $descending, int $startRow, int $fetchCount) : array
    {
        $retData = array();
        $query = "SELECT ##FIELDSLIST## FROM ##TABLENAME## "; // ADD WHERE CLAUSE FOR FILTER
        if (strlen($sortBy) > 0) {
            $query .= " ORDER BY " . $sortBy;
            if ($descending == 1) {
                $query .= " DESC";
            }
        }
        $query .= " LIMIT " . $startRow . ", " . $fetchCount;
        $stmt = $this->connection->prepare($query);
        $stmt->execute(); // REPLACE WHITE FILTER FIELDS
        if ($stmt->rowCount() > 0) {
            while ($row = $stmt->fetch()) {
                $rec = new ##TABLENAMECAP##(##FIELDSROW##);
                $retData[] = $rec;
            }
        }
        return $retData;
    }

    /**
     * {@inheritdoc}
     */
    public function insert(##TABLENAMECAP## $data): ##TABLENAMECAP##
    {
        $result = null;
        // Esegue l'insert dell'autore
        $query = "INSERT INTO ##TABLENAME##(##FIELDSLIST##) VALUES(##FIELDSPARAMS##)";
        $stmt = $this->connection->prepare($query);
        $params = array(##FIELDSINSERTARRAY##);
        if ($stmt->execute($params)) {
            $id = $this->connection->lastInsertId();
            $result = $this->get($id);
        }
        return $result;
    }

    /**
     * {@inheritdoc}
     */
    public function update(##TABLENAMECAP## $data): ##TABLENAMECAP##
    {
        $result = null;
        $query = "UPDATE ##TABLENAME## SET ##UPDATEFIELDS## WHERE ##WHEREKEY##";
        $stmt = $this->connection->prepare($query);
        $params = array(##UPDATEARRAY##);
        if ($stmt->execute($params)) {
            $result = $this->get(##KEYUPDATEPARAMS##);
        }
        return $result;
    }

    /**
     * {@inheritdoc}
     */
    public function delete(##KEYPARAMS##): bool
    {
        $ok = true;
        $query = "DELETE FROM ##TABLENAME## WHERE ##WHEREKEY##";
        $stmt = $this->connection->prepare($query);
        $params = array(##GETARRAY##);
        if ($stmt->execute($params)) {
            $ok = true;
        }
        return $ok;
    }

    /**
     * {@inheritdoc}
     */
    public function getCount(string $filtro): int
    {
        $query = "SELECT ##KEYFIELDS## FROM ##TABLENAME##"; // INSERT WHERE CLAUSE FOR FILTER
        $stmt = $this->connection->prepare($query);
        $stmt->execute(); // ADD FILTER PARAMS
        return $stmt->rowCount();
    }
}