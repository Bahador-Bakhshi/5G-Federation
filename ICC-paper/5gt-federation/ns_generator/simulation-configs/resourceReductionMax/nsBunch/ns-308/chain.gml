graph [
  node [
    id 0
    label 1
    disk 1
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 4
    memory 10
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 3
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
    bw 115
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 115
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 122
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 115
  ]
  edge [
    source 2
    target 5
    delay 29
    bw 174
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 177
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 102
  ]
]
