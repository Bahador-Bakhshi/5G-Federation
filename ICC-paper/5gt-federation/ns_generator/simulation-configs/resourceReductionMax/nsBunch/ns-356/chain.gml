graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 124
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 155
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 110
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 91
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 147
  ]
  edge [
    source 2
    target 5
    delay 26
    bw 193
  ]
]
