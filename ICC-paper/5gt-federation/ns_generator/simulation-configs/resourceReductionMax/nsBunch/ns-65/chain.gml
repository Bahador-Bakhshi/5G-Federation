graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 5
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 3
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 96
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 190
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 173
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 144
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 128
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 177
  ]
]
