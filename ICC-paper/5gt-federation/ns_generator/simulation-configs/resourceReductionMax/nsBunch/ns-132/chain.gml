graph [
  node [
    id 0
    label 1
    disk 9
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 56
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 176
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 187
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 109
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 151
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 123
  ]
]
