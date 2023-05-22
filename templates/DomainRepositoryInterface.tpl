<?php

declare(strict_types=1);

namespace App\Domain\##TABLENAME##;

use phpDocumentor\Reflection\Types\Boolean;

interface ##TABLENAME##Repository
{
    public function getAll(): array;

    public function getSubset(string $filtro, string $sortBy, int $descending, int $startRow, int $fetchCount): array;

    public function findByKey(##KEYFIELDS##): ##TABLENAME##;

    public function insert(##TABLENAME## $data): ##TABLENAME##;

    public function update(##TABLENAME## $data): ##TABLENAME##;

    public function delete(##KEYFIELDS##): bool;

    public function getCount(string $filtro): int;

}