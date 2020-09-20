graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 6
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 11
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 101
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 200
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 187
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 56
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 147
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 84
  ]
]
