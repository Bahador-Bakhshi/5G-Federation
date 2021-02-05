graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 11
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 5
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 52
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 166
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 170
  ]
  edge [
    source 1
    target 5
    delay 33
    bw 176
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 200
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 147
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 62
  ]
]
