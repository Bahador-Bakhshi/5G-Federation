graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 4
    memory 11
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 1
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 1
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 133
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 57
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 140
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 147
  ]
  edge [
    source 1
    target 5
    delay 30
    bw 89
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 113
  ]
]
