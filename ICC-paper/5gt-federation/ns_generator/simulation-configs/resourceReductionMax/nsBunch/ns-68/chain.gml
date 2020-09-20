graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 2
    memory 16
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 124
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 132
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 177
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 123
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 84
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 190
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 106
  ]
]
