graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 14
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 13
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 11
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 177
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 84
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 190
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 200
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 168
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 110
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 122
  ]
]
